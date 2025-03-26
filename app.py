from flask import Flask, render_template, jsonify, request

app = Flask(__name__)



# 页面路由
@app.route('/')
def index():
    return render_template('search-results.html')


@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.get_json()
    if 'array[]' in data:
        array_data = data['array[]']
        # 在这里处理数组数据
        print("Received array:", array_data)
        return jsonify({"message": "Data received", "array": array_data})
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
    app.run(debug=True)
