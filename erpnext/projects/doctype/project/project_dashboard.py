from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the Time Sheets created against this project'),
		'fieldname': 'project',
		'transactions': [
			{
				'label': _('Project'),
				'items': ['Task', 'Timesheet', 'Expense Claim', 'Issue']
			},
			{
				'label': _('Material'),
				'items': ['Material Request', 'BOM', 'Stock Entry']
			},
			{
				'label': _('Sales'),
<<<<<<< HEAD
				'items': ['Sales Order', 'Delivery Note', 'Sales Invoice']
=======
				'items': ['Sales Invoice']
>>>>>>> 95d706d57b6cac6113b64196e32dafd821e302b7
			},
			{
				'label': _('Purchase'),
				'items': ['Purchase Order', 'Purchase Receipt', 'Purchase Invoice']
			},
		]
	}
