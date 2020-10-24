# BENCHOP as a Service (BaaS), Group Project Group 4, Applied Cloud Computing HT20

## How to use BaaS:
- clone the repository.
- for the master node, run 
    `orchestration/main_vm.sh`. 
  This will also start the Flask app for the RESTful API calls.
- for the setup of the worker nodes, run 
    `python3 orchestration/ssc-cloudinit.py`
*Important*: Set the path to your key in the file!

- curl with the routing `/benchop`. Enjoy!



