# Howl

##Database
https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd


with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)

INSERT
        INTO
        `ALLOWANCE`(`EmployeeID`, `Year`, `Month`, `OverTime`, `Medical`,
                    `Lunch`, `Bonus`, `Allowance`)
        values(10000001, 2014, 4, 10.00, 10.00,
               10.45, 10.10, 40.55)
        ON
        DUPLICATE
        KEY
        UPDATE
        `EmployeeID` = 10000001