from flask import Flask, render_template, jsonify, request
import torch
import sys

app = Flask(__name__)

app.recommender_sys = torch.load("EEDN_Yelp.pth")
app.recommender_sys.to('cuda:0')
app.recommender_sys.eval()
import Items
app.items = {}
for item in Items.ITEMS:
    app.items[item['id']] = item

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', stream=sys.stdout)
logger = logging.getLogger()


# 页面路由
@app.route('/')
def index():
    return render_template('search-results.html')

@app.route('/item', methods=['POST'])
def item():
    data = request.get_json()
    item = app.items[data['id']]
    return jsonify({'item': item})


@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.get_json()
    if 'array[]' in data:
        array_data = data['array[]']
        # print(array_data)
        event_type = torch.tensor([int(item_id) for item_id in array_data], dtype=torch.long)
        event_type = event_type.to(torch.device('cuda:0')).unsqueeze(0)
        prediction, _ = app.recommender_sys(event_type)
        recommended_items = torch.topk(prediction, 10, -1, sorted=True)[1]
        recommended_items = recommended_items[0].cpu().tolist()
        results = []
        for idx in recommended_items:
            results.append(app.items[idx])

        # remote_addr = request.remote_addr
        # logger.info('[' + remote_addr + "] Received array:")
        # logger.info(array_data)
        # logger.info('[' + remote_addr + "] Recommended items:")
        # logger.info(recommended_items)
        return jsonify({"message": "Data received", "array": results})
    else:
        return jsonify({"error": "No array data found"}), 400



# AJAX 数据接口
@app.route('/data', methods=['GET'])
def get_data():
    # 从请求中获取参数（可选）
    param = request.args.get('param', 'default')

    # 返回模拟数据
    data = {
        'message': f'Hello, {param}!',
        'status': 'success',
        'data': [1, 2, 3, 4, 5]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
