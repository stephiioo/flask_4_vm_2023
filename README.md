# flask_4_vm_2023

## azure virtual machine set up process:


### step 1: open up microsoft azure and sign in


### step 2: type in Virtual Machine into the search bar, click on it and when it opens up, hit "create" and then of the two options present, click "virtual machine"


### Step 3: configure the VM appropriately so that it has the cost option of $15.11


#### some key configurations to note:

#### resource group: i saved my vm to a previously created resource group called "stephanie-504"

#### region: us east

#### image: ubuntu server gen 2

#### size: standard b1ms 1 vcpu 2 gib

#### authetication type: click password and enter preferred username and password

#### vm network ports: http (80), https (443), ssh (22)

#### enable auto-shutdown at set to 11:59pm east (us & canada)


### step 4: rveiew and create VM


## VM setup process:

### step 1: open cloud shell

### step 2: in the cloud shell terminal, enter:

#### - pwd

#### - ssh sogbebor@52.186.170.255 (which is the ip address for the azure VM)

#### - type "yes", hit enter, then type in your password and hit enter

#### your cloud shell should now say "sogbebor@mysql-vm:~$:

### step 3: type "sudo apt-get update"

### step 4: type "sudo apt install mysql-server mysql-client" then type "Y" when prompted

### step 5: type "sudo MySQL" which will allow the terminal to display "MySQL>"


### rationale for schema: honestly the reason I chose to create "patients", "doctors' and "appointments" is because those were the first tings that I thought of and it just seemed like the most ideal to do

### challenges; i kept getting error messages and when I finally got the patients, doctors, and appointment tabs to open up, I couldn't get it to populate with fake data.
