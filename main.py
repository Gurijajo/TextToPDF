from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Store:
    def __init__(self, name, monthly_income):
        self.name = name
        self.monthly_income = monthly_income

def get_store_info():
    stores = []
    for i in range(1, 11):
        name = input(f"Enter the name of store {i} (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        monthly_income = float(input(f"Enter the monthly income of {name}: $"))
        store = Store(name, monthly_income)
        stores.append(store)
    return stores

def calculate_average_annual_income(stores):
    total_income = 0
    for store in stores:
        total_income += store.monthly_income * 12
    return total_income / len(stores)

def generate_pdf(stores, average_income):
    filename = "store_income_report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Store Income Report")
    c.drawString(100, 730, "---------------------")
    y = 700
    for store in stores:
        c.drawString(100, y, f"{store.name}: ${store.monthly_income:,.2f} monthly")
        y -= 20
    c.drawString(100, y-20, f"Average Annual Income: ${average_income:,.2f}")
    c.save()
    print(f"PDF report saved as '{filename}'.")

def main():
    print("Welcome to the Store Income Calculator!")
    stores = get_store_info()
    if not stores:
        print("No stores entered.")
        return
    average_income = calculate_average_annual_income(stores)
    generate_pdf(stores, average_income)

if __name__ == "__main__":
    main()
