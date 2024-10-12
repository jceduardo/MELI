# Challenge 1

**Test Data and Output**

| Row | First City  | Second City   | Output                                      |
|-----|-------------|---------------|---------------------------------------------|
|  1  | Pune        | New Delhi     | Indian Institute of Technology Delhi (IITD) |
|  2  | Cambridge   | Santiago      | University of Cambridge                     |
|  3  | Zürich      |               | Sorbonne University                         |
|  4  | London      |               | UCL                        |
|  5  |             |               | Sorbonne University                         |
|  6  | None        |               | Sorbonne University                         |
|  7  |             | None          | Sorbonne University                         |
|  8  | None        | None          |                                             |
|  9  | MockCity1   | MockCity2     |                                             |

**Output Script**

| 1.Indian Institute of Technology Delhi (IITD) | 
| 2.University of Cambridge                     | 
| 3.Sorbonne University                         |  
| 4.UCL                                         | 
| 5.Sorbonne University                         | 
| 6.Sorbonne University                         | 
| 7.Sorbonne University                         | 
| 8.                                            | 
| 9.                                            | 

# Challenge 2

**Database**

-- Table: customers
```
CREATE TABLE customers (
    id SMALLINT PRIMARY KEY,
    first_name VARCHAR(64),
    last_name VARCHAR(64)
);
```

-- Table: campaigns
```
CREATE TABLE campaigns (
    id SMALLINT PRIMARY KEY,
    customer_id SMALLINT,
    name VARCHAR(64),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

-- Table: events
```
CREATE TABLE events (
    dt VARCHAR(19),
    campaign_id SMALLINT,
    status VARCHAR(64),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
);
```

**Test Data**

```
INSERT INTO customers (id, first_name, last_name) VALUES(1, 'Whitney', 'Ferrero');

INSERT INTO customers (id, first_name, last_name) VALUES(2, 'Dickie', 'Romera');

INSERT INTO customers (id, first_name, last_name) VALUES(3, 'John', 'Edward');


INSERT INTO campaigns (id, customer_id, name) VALUES(1, 1, 'Upton Group');

INSERT INTO campaigns (id, customer_id, name) VALUES(2, 1, 'Roob, Hudson and Rippin');

INSERT INTO campaigns (id, customer_id, name) VALUES(3, 1, 'McCullough, Rempel and Larson');

INSERT INTO campaigns (id, customer_id, name) VALUES(4, 1, 'Lang and Sons');

INSERT INTO campaigns (id, customer_id, name) VALUES(5, 2, 'Ruecker, Hand and Haley');

INSERT INTO campaigns (id, customer_id, name) VALUES(6, 3, 'Co-Workers Together');


INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 13:52:00', 1, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 08:17:48', 2, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 08:18:17', 2, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 11:55:32', 3, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 06:53:16', 4, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 04:51:09', 4, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 06:34:04', 5, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 03:21:18', 5, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 03:18:24', 5, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 15:32:37', 1, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 04:23:20', 1, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 06:53:24', 1, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 08:01:02', 2, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 15:57:19', 2, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 16:14:34', 3, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 21:56:38', 3, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 05:54:43', 4, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 17:56:45', 4, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 11:56:50', 4, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 06:08:20', 5, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 06:08:20', 6, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 07:18:20', 6, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 08:15:20', 6, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 12:30:20', 6, 'failure');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 09:00:20', 6, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 13:21:20', 6, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 06:17:20', 6, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 14:09:20', 6, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-01 06:11:20', 6, 'success');

INSERT INTO events (dt, campaign_id, status) VALUES('2021-12-02 17:45:20', 6, 'success');

COMMIT;
```

**Execution Result**

| Whitney, 6 | 
| John, 4    | 


