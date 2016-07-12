# Insight Code Challenge - Streaming Venmo Transaction

This project is created for Insight Data Engineering Code Challenge.
It processes venmo transaction files line by line and updates a single-edge graph and calculates the streaming median.

### Assumptions:
* This project considers 60s exclusive.

* User names are NOT case-sensitive.

* If multiple transactions occurred between the same two users, we update the edge with the latest valid time within the window.

### Packages and Versions

This project is compiled with Python 2.7.6.
Additional packages include numpy(1.8.0rc1) and networkx(1.11)

#### Installation
* _numpy_ installation:
pip install numpy

* _networkx_ installation:
sudo pip install networkx

### Running the tests

All tests are located under insight_testsuite.

Run _insight_testsuite/run_tests.sh_ to execute all test cases. Test results are output to console. Program results are output to each venmo_output folder accordingly.

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

To test out if there are transactions between the same two users that occurred within one minute.

```
{"created_time": "2016-03-28T23:23:13Z", "target": "Tyrion-Lannister", "actor": "Jon-Snow"}
{"created_time": "2016-03-28T23:23:14Z", "target": "Tyrion-Lannister", "actor": "Jon-Snow"}

```
Expected output:
```
1.00
1.00
```

**test-3-venmo-trans**

Records that has multiple transactions between 2 same users and spread outside of 60s window.

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
2.00
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

**test-5-venmo-trans**

To rule out lines with incorrect time format.

```
{"created_time": "2016-03-28T23:23:12Za", "target": "Tyrion-Lannister", "actor": "Little-Finger"}
{"created_time": "2016-03-28T23:23:12Z", "target": "Little-Finger", "actor": "Tyrion-Lannister"}
{"created_time": "2016-03-28T23:24:11Z", "target": "Tyrion-Lannister", "actor": "Little-Finger"}
{"created_time": "2016-03-28T23:24:12Z", "target": "Tyrion-Lannister", "actor": "Cersei-Lannister"}
{"created_time": "2016-03-28T23:24:13Z", "target": "Little-Finger", "actor": "Cersei-Lannister"}

```
Expected output:
```
1.00
1.00
1.00
2.00

```


## Authors

* **Ying Huang**

