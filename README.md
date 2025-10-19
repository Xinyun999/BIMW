# BIMW: Blockchain-Enabled Innocuous Model Watermarking for Secure Ownership Verification

## Introduction
This is the implementation for our paper "[BIMW: Blockchain-Enabled Innocuous Model Watermarking for Secure Ownership Verification]"

**Getting Start**
<pre>
conda create -n BIMW python=3.8
conda activate BIMW
</pre>

Install the necessary packages to run BIMW, including pytorch, opencv-python, tqdm, piqa, and scipy.
<pre>
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
pip install opencv-python
pip install tqdm
pip install piqa
pip install scipy
</pre>

To train a ResNet-18 model 
<pre>
bash classification/scripts/pretrain.sh {gpus}
</pre>

Embed the watermark into the pre-trained model. 
<pre>
bash classification/scripts/embed.sh {model_path} {wm_length} {wm_path} {gpus}
</pre>

Extract the watermark from the watermarked model.
<pre>
bash classification/scripts/test.sh {model_path} {wm_length} {wm_path} {trigger_path} {gpus}
</pre>

The model watermarking code is inspired by [EaaW](https://github.com/shaoshuo-ss/EaaW).

## Blockchain Protection

Run IPFS test network.
Refer to "Blockchain/IPFS"

You can run local miners as test network.
Refer to "Blockchain/boot_network"

**Compile and deploy contract on Ethereum network.**
1. You need check these points:

-- ensure local miners are running

-- enable networks->development in ./truffle-config.js

-- correct deploy functions in ./migrations/1_deploy_contracts.js

2. Compile contracts and migrate to local network.
<pre>
// compile contracts
truffle compile	

// deploy contracts on local network (You need properly setup networks->development in truffle-config.js)
truffle migrate --reset
</pre>

**Demo and test cases.**
1. Update configuration data in "./src/config/addr_list.json".

--- HttpProvider: replace with you local geth interface 'ip:port'

--- NFT_Data: replace with deployed contract address

--- host_account: input coinbase account used in your local geth node.

2. To test on local network, you can try following commands.

<pre>
cd src
// execute test_demo.py containing demo and performance evaluation
python3 test_demo.py -h  													// get usages
python3 test_demo.py --test_func 0											// display main account and data tokens.
python3 test_demo.py --test_func 1 --id 1									// query by id 
python3 test_demo.py --test_func 2 --value host_account --tx_round 10		// mint tokens by owner, ids range in [args.id+1, args.id+10]
python3 test_demo.py --test_func 2 --value other_account					// mint a token by other, use default id=1
python3 test_demo.py --test_func 3 --value host_account --tx_round 10		// burn tokens by owner, ids range in [args.id+1, args.id+10]
python3 test_demo.py --test_func 4  --value 10 --op_status 1 --tx_round 5	// Use 10 figures in folder "src/test_fig" to create MKT of frames and save results into a token with ids range in [args.id+1, args.id+10]
python3 test_demo.py --test_func 5 --op_status 1 --tx_round 5 				// Audit token data ids range in [args.id+1, args.id+10]
</pre>
4. To test on webservice, you can try following commands.
<pre>
cd src

// execute server app
python3 NFT_Server.py

// execute client app to run test cases			
python3 Test_Client.py -h  							// get usages
python3 Test_Client.py --test_func 0 				// query main account and data tokens. 
python3 Test_Client.py --test_func 1 --id 5 		// query a token by id=5
python3 Test_Client.py --test_func 2 --id 1 --thread_count 10 --tx_round 2 		// bindle multiple token query (threads) in a process, ids range in [args.id+1, args.id+10], repeat test count: 2.
</pre>

