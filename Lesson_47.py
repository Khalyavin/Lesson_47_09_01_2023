import csv
import psycopg2


customers_file = 'customers_data.csv'
employees_file = 'employees_data.csv'
orders_file = 'orders_data.csv'


def main():
    """Connect to database, fill 3 tables from customers files"""
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='1'
    )

    try:
        with conn:
            with conn.cursor() as cur:
                fp = open(employees_file, 'r', encoding='UTF-8')
                f_reader = csv.reader(fp)

                # header - out
                header = next(f_reader)
                for row in f_reader:
                    rec_to_insert = (row[0], row[1], row[2], row[3], row[4])
                    query = "INSERT INTO employees(first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)"
                    cur.execute(query, rec_to_insert)

                fp.close()

            # Employee table filled
            # Out of WITH xxx as cur: - cursor closed, connection ready for filling next file

            with conn.cursor() as cur:
                fp = open(customers_file, 'r', encoding='UTF-8')
                f_reader = csv.reader(fp)

                # header - out
                header = next(f_reader)
                for row in f_reader:
                    rec_to_insert = (row[0], row[1], row[2])
                    query = "INSERT INTO customers VALUES (%s, %s, %s)"
                    cur.execute(query, rec_to_insert)

                fp.close()

            # Customers table filled
            # Out of WITH xxx as cur: - cursor closed, connection ready for filling next file

            with conn.cursor() as cur:
                fp = open(orders_file, 'r', encoding='UTF-8')
                f_reader = csv.reader(fp)

                # header - out
                header = next(f_reader)
                for row in f_reader:
                    rec_to_insert = (row[0], row[1], row[2], row[3])
                    query = "INSERT INTO customers VALUES (%s, %s, %s, %s)"
                    cur.execute(query, rec_to_insert)

                fp.close()

            # Orders table filled
            # Out of WITH xxx as cur: - cursor closed, connection closed in finally

    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()