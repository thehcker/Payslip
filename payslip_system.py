employees = dict()
slips  = dict()
basic_salary =  10000




def file_employeedetails():
	global employees
	name = input("Enter employee name: ")
	kra_pin = input("Enter employee's KRA pin: ")

	employees[name] = [name, kra_pin]   

def update_sales_record(employee_name):

	quantity =  input("Enter Quantity sold: ")
	amount  = input("Payment : ")

	try:
		amount = float(amount)
		quantity =float(quantity)
	except:
		pass

	com = (quantity *amount) * (10/100) 

	employees[employee_name].append(amount)
	employees[employee_name].append(quantity)
	employees[employee_name].append(com)
	generate_slip(employee_name)



def calculate_tax(employee_name):
	gross = basic_salary + employees[employee_name][4]
	employees[employee_name].append(gross)

	tax = None

	if gross > 100000:
		tax = .25
	elif gross > 50000:
		tax = .2
	elif gross > 30000:
		tax = .15
	elif gross > 10000:
		tax = .1
	elif gross > 5000:
		tax = .05
	else:
		tax = 0

	return tax

def net_salary(employee_name):
	net = (employees[employee_name][5]  * calculate_tax(employee_name) )
	return net



def generate_slip(employee_name):
	global slips 
	details = employees[employee_name]
	name = details[0]
	pin =  details[1]
	tax = calculate_tax(employee_name)
	net  = net_salary(employee_name)
	amount = details[2]
	gross  = details[5]
	slip = f"""
 ----------------------------------------------------------------------
 :		JUMIA ENTERPRISE PAYROLL SLIP	                             :
 ----------------------------------------------------------------------
 Name:  {name}                  KRA Pin: {pin}
 -----------------------------------------------------------------------
 : Hours 		Quantity sold             Amount                      :                     
 -----------------------------------------------------------------------


 Tax Rate:      {tax*100 }%             Tax Due: Ksh. {amount}         :
 -----------------------------------------------------------------------
 Gross Salary: Ksh {gross}			Net Sal: Ksh. {net}      :
 -----------------------------------------------------------------------

"""
	
	slips[employee_name] = slip

	
def print_payslip(employee_name):
	slip =  slips[employee_name]
	print(slip)


def print_all_slips():
	global slips

	for slip in slips.values():
		print(slip)

def get_gross_salary(employee_name):
	pass

if __name__ == "__main__":
	running = True


	while running:
		task = input("Enter a command: ")

		if task == "add employee":
			file_employeedetails()

		elif task == "update records":
			name = input("For which employee: ")
			update_sales_record(name)

		elif task == "print slip":
			name = input("For whom: ")
			generate_slip(name)
			print_payslip(name)

		elif task == "print all":
			print_all_slips()

		elif task == "quit":
			running = False
		else:
			print("Sorry, I am not programed to perfom this task ")
			print(f"I literaly cant {task}")

		