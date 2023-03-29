from jinja2 import Environment, FileSystemLoader

# Load the Jinja templates
env = Environment(loader=FileSystemLoader('templates'))
sales_report_template = env.get_template('sales_report_template.html')

# Generate the report using the merged data
sales_report_html = sales_report_template.render(data=merged_data)

# Save the report as an HTML file
with open('sales_report.html', 'w') as f:
    f.write(sales_report_html)
