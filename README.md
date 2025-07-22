## Recommender System Demo

---
### - Instruction (Download [[EEDN_Yelp.pth]](https://drive.google.com/file/d/109j7r9mZBcm3nTNaK54PLl16l2HKOGBU/view?usp=sharing))

    ### Run Demo
    >> python app.py

    ### Access Website (Change 127.0.0.1 to the target server IP)
    http://127.0.0.1:5000
    
---------------------------------------------

---
### - Train EEDN_Yelp.pth by yourself

    # Train
    >> python Main.py

    
---------------------------------------------

### - If you want to Change the Dataset

    # 1. Revise Setup in Contants.py 
    # 2. Train the EEDN
    >> python Main.py

    # 3. Update static/item.js (for web end)
    # 4. Update Items.py (for server end)
    # 5. Run the Demo
    >> python app.py

---
### - Install requirements (Download [[requirements.txt]](https://github.com/WangXFng/NFARec/blob/main/requirements.txt))
    # 1. create a conda environment
    >> conda create -n myenv python=3.10
    # 2. activate the environment
    >> conda activate myenv
    # 3. instaill torch according to your Nvidia driver (!! An example)
    >> pip3 install torch torchvision torchaudio
    # 4. install requirements.txt
    >> pip install -r requirements.txt
