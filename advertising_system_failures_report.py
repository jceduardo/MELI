import mysql.connector
from mysql.connector import Error

def calculateFailureEvents(cursor):
    cursor.execute(
        """
            select 
 	            cus.first_name, 
                count(eve.status) as quantity
            from 
                customers cus,  
                campaigns cam,
                events eve 
            where
                cus.id = cam.customer_id and 
                cam.id = eve.campaign_id and 
                eve.status = 'failure'
            group by 
                cus.first_name
            having 
                quantity > 3
        """
    )

    # Retrieve all events rows from the results of the query
    event_records = cursor.fetchall()

    events = []
    for row in event_records:
        event = {
            'firstName': row[0], 
            'quantity': row[1]
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

            # Calculate number of failures grouping by customer's first name 
            events = calculateFailureEvents(cursor)

            print("customer    failures")
            print("========    ========")
            for customer in events:
                firstName = customer['firstName']
                print(f"{firstName}" + (12 - len(firstName)) * ' ' + f"{customer['quantity']}")

    except Error as e:
        print(f"Database error: {e}")
    
    finally:
        # Close connection
        if connection.is_connected(): 
            cursor.close()
            connection.close()

if __name__ == "__main__":
    failures_report()