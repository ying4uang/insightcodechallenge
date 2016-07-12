# Insight Code Challenge - Streaming Venmo Transaction

This project is created to answer the Insight Data Engineering Code Challenge.
It processes venmo transaction files line by line and updates a multi-edge graph and calculates the streaming median.

### Assumptions:
* This projects considers the 60s inclusive.
For instance, if one transacation occurred at 10h40m10s and another one at 10h41m10s we consider these two transactions within the 60s window.
* This project assumes that multiple transactions can happen between same people within the 60s window.

### Packages and Versions

This project is compiled with Python 2.7.6.
Additional packages include numpy(1.8.0rc1) and networkx(1.11)

#### Installation
* _numpy_ installation
pip install numpy
* _networkx_ installation
sudo pip install networkx

### Running the tests

All tests are located under insight_testsuite.

Run _run_tests.sh_ to execute all test cases. Test outputs are under venmo_output folder under each test folder.

**test-1-venmo-trans**

This is the orginial test case given in the challnge
```
{"created_time": "2016-04-07T03:33:19Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}
```
Expected output:
```
1.00
```

**test-2-venmo-trans**

To test out if there are transactions between the same people that occurred within one minute.

```
{"created_time": "2016-03-28T23:23:13Z", "target": "Tyrion-Lannister", "actor": "Jon-Snow"}
{"created_time": "2016-03-28T23:24:13Z", "target": "Tyrion-Lannister", "actor": "Jon-Snow"}

```
Expected output:
```
1.00
2.00
```

**test-3-venmo-trans**

Records that has 2 transactions between same people and spread outside of 60s window. This is to make sure we are not removing evicting the valid transcations occurred within 60s window.

```
{"created_time": "2016-03-28T23:23:12Z", "target": "Tyrion-Lannister", "actor": "Little-Finger"}
{"created_time": "2016-03-28T23:23:12Z", "target": "Ned-Stark", "actor": "Little-Finger"}
{"created_time": "2016-03-28T23:23:12Z", "target": "Ramsey-Bolton", "actor": "Little-Finger"}
{"created_time": "2016-03-28T23:23:12Z", "target": "Ned-Stark", "actor": "Tyrion-Lannister"}
{"created_time": "2016-03-28T23:23:13Z", "target": "Tyrion-Lannister", "actor": "Little-Finger"}
{"created_time": "2016-03-28T23:24:13Z", "target": "Tyrion-Lannister", "actor": "Little-Finger"}

```
Expected output:
```
1.00
1.00
1.00
2.00
2.50
2.00

```

**test-4-venmo-trans**

To ensure empty lines are not stopping the program from executing and the names are not case-sensitive.

```
{"created_time": "2016-03-28T23:23:12Z", "target": "Tyrion-lannister", "actor": "Little-Finger"}

{"created_time": "2016-03-28T23:23:12Z", "target": "Ned-Stark", "actor": "Tyrion-Lannister"}

```
Expected output:
```
1.00
1.00

```




### Installing

A step by step series of examples that tell you have to get a development env running

Stay what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```



## Authors

* **Ying Huang** - *Initial work*

