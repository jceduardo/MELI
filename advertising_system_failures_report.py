import mysql.connector
from mysql.connector import Error

def load_customers(cursor):
    cursor.execute("SELECT * FROM customers")
            
    # Get all customers
    records = cursor.fetchall()

    customers = []
    for row in records:
        customer = {
            'id': row[0], 
            'firstName': row[1], 
            'lastName': row[2]
        }
        customers.append(customer)  

    return customers

def load_campaigns(cursor):
    cursor.execute("SELECT * FROM campaigns")
            
    # Get all campaigns
    campaign_records = cursor.fetchall()

    campaigns = []
    for row in campaign_records:
        campaign = {
            'id': row[0], 
            'customerId': row[1], 
            'name': row[2]
        }
        campaigns.append(campaign)

    return campaigns

def load_events(cursor, customers, campaigns):
    cursor.execute("SELECT * FROM events")

    # Get all events
    event_records = cursor.fetchall()

    events = []
    for row in event_records:
        customer_id = 0
        for campaign in campaigns:
            if campaign['id'] == row[1]:
                customer_id = campaign['customerId']
                break
        customer_name = ''
        for customer in customers:
            if customer['id'] == customer_id:
                customer_name = customer['firstName']
                break
        event = {
            'dt': row[0], 
            'campaignId': row[1], 
            'status': row[2],
            'customerName': customer_name
        }
        events.append(event) 

    return events

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',        
            database='db_advertising_failures',  
            user='******',       
            password='******'  
        )

    except Error as e:
        print(f"Error connecting to database: {e}")

    return connection

def failures_report():
    try:
        # Connect to database
        connection = connect_to_database()

        if connection.is_connected():            
            # Create cursor in order to execute queries
            cursor = connection.cursor()

            # Load customers
            customers = load_customers(cursor)      

            # Load campaigns
            campaigns = load_campaigns(cursor)

            # Load events
            events = load_events(cursor, customers, campaigns)
            
            # Dictionary to store results
            resultado = {}

            # Group by customer's name
            for item in events:
                customerName = item['customerName']                
                if customerName not in resultado:
                    resultado[customerName] = 0
                if item['status'] == 'failure':
                    resultado[customerName] += 1

            for customerName, quantity in resultado.items():
                if quantity > 3: # Filter customers with more than 3 events with status = 'failure'
                    print(f"{customerName}, {quantity}")

    except Error as e:
        print(f"Database error: {e}")
    
    finally:
        if connection.is_connected(): # Close connection
            cursor.close()
            connection.close()

if __name__ == "__main__":
    failures_report()