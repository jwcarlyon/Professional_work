## Example Server
Maven Spring project which currently loads a secure servlet backend with a REST controller and some hardcoded data. REACT JavaScript front_end is located src/main/web and creates a working GUI with some REST calls to show functionality
### Running Locally
Using bash enter the one of following commands
- `mvn package` This will build the project if you have not already.  
- `mvn spring-boot:run` This will deploy the project

### Driver API
This is a springBoot project that sets up a database of formula 1 stats. When deployed,  
the application will create a relational database of F1 Drivers with a controller for  
recalling the saved Driver as JSON. Read the WEB folder to set up the front end and see  
the DriverStatsPage.

### TODO!

Add times/eta for each race and driver... seems like a Race DB may be necessary? 
