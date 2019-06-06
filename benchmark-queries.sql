-- initial queries for measuring the benchmarks devised in part 2

-- Experiment 1
/*
    the 10% rule of thumb

    Create a 100k tuple - Done
*/
-- Query 2 and 4
SELECT * 
FROM wisc.HUNDREDKTUP1
WHERE unique2 BETWEEN 792 AND 1791;

-- Index for query 4
CREATE INDEX idx_hund_uniq2
ON wisc.HUNDREDKTUP1(unique2);

-- Index for query 6
CREATE INDEX idx_hund_uniq1
ON wisc.HUNDREDKTUP1(unique1);

-- Query 6
SELECT * 
FROM wisc.HUNDREDKTUP1
WHERE unique1 BETWEEN 792 AND 1791;

/*
----------------------------------------------------
*/


-- Experiment 2
/*
    join algorithms - hash vs sort/merge
*/

-- Create BPrime
CREATE TABLE IF NOT EXISTS wisc.BPRIME (
    unique1         integer NOT NULL,
    unique2         integer NOT NULL PRIMARY KEY,
    two             integer NOT NULL,
    four            integer NOT NULL,
    ten             integer NOT NULL,
    twenty          integer NOT NULL,
    onePercent      integer NOT NULL,
    tenPercent      integer NOT NULL,
    twentyPercent   integer NOT NULL,
    fiftyPercent    integer NOT NULL,
    unique3         integer NOT NULL,
    evenOnePercent  integer NOT NULL,
    oddOnePercent   integer NOT NULL,
    stringu1        char(52) NOT NULL,
    stringu2        char(52) NOT NULL,
    string4         char(52) NOT NULL
);

-- Populate BPrime
INSERT INTO BPRIME 
SELECT * 
FROM TENKTUP2 
WHERE TENKTUP2.unique2 < 1000;

-- Query 10 and 13
SELECT * 
FROM wisc.TENKTUP1, wisc.BPRIME 
WHERE (wisc.TENKTUP1.unique2 = wisc.BPRIME.unique2)

-- Query 15
SELECT * 
FROM wisc.TENKTUP1, wisc.TENKTUP2 
WHERE (wisc.TENKTUP1.unique1 = wisc.TENKTUP2.unique1) 
AND (wisc.TENKTUP1.unique2 < 1000)

-- Query 17
SELECT * 
FROM wisc.ONEKTUP, wisc.TENKTUP1, wisc.TENKTUP2
WHERE (wisc.ONEKTUP.unique1 = wisc.TENKTUP1.unique1) 
AND (wisc.TENKTUP1.unique1 = wisc.TENKTUP2.unique1) 
AND (wisc.TENKTUP1.unique1 < 1000)


/*
----------------------------------------------------
*/


-- Experiment 3
/*
    aggregation
*/

-- Query 22 and 25
SELECT SUM (wisc.TENKTUP1.unique3) 
FROM wisc.TENKTUP1 
GROUP BY wisc.TENKTUP1.onePercent

-- Query 4
/*
    GEQO Query Optimization
*/

-- Query 10

SELECT * 
FROM wisc.TENKTUP1, wisc.BPRIME, wisc.HUNDREDKTUP1, wisc.ONEKTUP
WHERE (wisc.TENKTUP1.unique2 = wisc.BPRIME.unique2)
AND (wisc.HUNDREDKTUP1.onePercent = wisc.BPRIME.onePercent)
AND (wisc.ONEKTUP.unique3 = wisc.BPRIME.unique2)

SELECT * 
FROM wisc.TENKTUP1, wisc.BPRIME, wisc.HUNDREDKTUP1 --, wisc.ONEKTUP
WHERE (wisc.TENKTUP1.unique2 = wisc.BPRIME.unique2)
AND (wisc.HUNDREDKTUP1.onePercent = wisc.BPRIME.onePercent)
--AND (wisc.ONEKTUP.unique3 = wisc.BPRIME.unique2)
