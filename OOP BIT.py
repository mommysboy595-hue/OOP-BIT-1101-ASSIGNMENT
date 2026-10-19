# ==========================================
# DOMAIN: Agriculture (Smart Farm & Crop Monitoring System)
# ==========================================

class FarmPlot:
    """Represents a specific section or plot of land on a farm."""

    def __init__(self, plot_id, soil_type):
        self.plot_id = plot_id
        self.soil_type = soil_type

    def get_plot_summary(self):
        return f"Plot ID: {self.plot_id} (Soil: {self.soil_type})"


class Farmer:
    """Represents a farmer managing agricultural data (Task 1: OOP Basics)."""

    # Class attribute to keep track of total active farmers in the system
    total_farmers = 0

    def __init__(self, farmer_id, name, region):
        self.farmer_id = farmer_id  # Unique ID
        self.name = name  # Farmer Name
        self.region = region  # Region / Location
        self.harvest_records = []  # List to hold harvest logs

        # Increment total farmers whenever a new object is created
        Farmer.total_farmers += 1

    # Task 3: Instance Method (operates on specific object data)
    def log_harvest(self, farm_plot, crop_name, yield_tons):
        """Log a harvest using a Tuple (plot, crop_name, yield_tons) for extra marks."""
        harvest_entry = (farm_plot, crop_name, yield_tons)
        self.harvest_records.append(harvest_entry)
        print(f"Recorded harvest for {self.name}: {yield_tons} tons of {crop_name} on {farm_plot.get_plot_summary()}")

    # Task 1 & 3: Instance Method to display farmer details
    def display_info(self):
        print(f"\n--- Farmer Profile & Yield Report ---")
        print(f"Farmer ID: {self.farmer_id}")
        print(f"Name: {self.name}")
        print(f"Region: {self.region}")
        print("Harvest Records:")
        if not self.harvest_records:
            print("  No harvests logged yet.")
        else:
            for plot, crop, tons in self.harvest_records:
                print(f"  - {plot.get_plot_summary()} | Crop: {crop} | Yield: {tons} Tons")

    # Task 3: Class Method (operates on class-level attributes)
    @classmethod
    def get_total_farmers_count(cls):
        return f"Total Registered Farmers in System: {cls.total_farmers}"


# ==========================================
# Task 2: Python Data Structures & Functions
# ==========================================

# Using a Dictionary to store farmers with their unique ID as the key
farmer_database = {}


def register_farmer(farmer_id, name, region):
    """Function to add a new farmer record to the dictionary."""
    if farmer_id in farmer_database:
        print(f"Error: Farmer with ID {farmer_id} already exists!")
    else:
        new_farmer = Farmer(farmer_id, name, region)
        farmer_database[farmer_id] = new_farmer
        print(f"Farmer {name} registered successfully!")


def display_all_farmers():
    """Function to loop through the dictionary and display all records."""
    if not farmer_database:
        print("No farmer records found.")
        return

    print("\n========================================")
    print("      AGRICULTURAL EXTENSION REGISTRY   ")
    print("========================================")
    for farmer_id, farmer_obj in farmer_database.items():
        farmer_obj.display_info()
    print("========================================")


# ==========================================
# Example Usage / Sample Program Execution
# ==========================================
if __name__ == "__main__":
    print("--- 1. Registering Farmers Using Functions ---")
    register_farmer("F001", "Mariatu Bangura", "Northern Province")
    register_farmer("F002", "Alpha Jalloh", "Southern Province")

    print("\n--- 2. Creating Farm Plot Objects ---")
    plot1 = FarmPlot("P-101", "Loam")
    plot2 = FarmPlot("P-102", "Clay-Loam")

    print("\n--- 3. Logging Harvests Using Instance Methods & Tuples (Extra Marks) ---")
    farmer_database["F001"].log_harvest(plot1, "Rice", 4.5)
    farmer_database["F001"].log_harvest(plot2, "Cassava", 6.2)

    farmer_database["F002"].log_harvest(plot1, "Maize", 3.8)

    print("\n--- 4. Displaying All Records (Task 2 Loop) ---")
    display_all_farmers()

    print("\n--- 5. Using Class Method ---")
    print(Farmer.get_total_farmers_count())