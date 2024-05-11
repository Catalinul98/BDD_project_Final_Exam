**_Project Name: BDD-project**_

**Project Overview**

The BDD-Project is designed to systematically test the UI functionalities of an e-commerce website using a Behavior Driven Development (BDD) approach.
By integrating Python with the Selenium framework, this project executes a series of automated tests on the [e-commerce demo site](https://magento.softwaretestingboard.com/) to verify user interaction and system responses according to predefined scenarios.


**Key Functionalities Tested**

**Shopping Cart Functionality:** Ensures users can add and remove items from the shopping cart and verifies related success messages.

**Login Functionality:** Tests login processes and error handling for incorrect user credentials.

**Registration Functionality:** Confirms the accuracy of the user registration process from start to finish.

**Search Functionality:** Assesses search operations, including the handling of non-existent products and product sorting.

**Prerequisites**

 - Language Used: I used Python for the described project. Python is often chosen for automated testing projects due to its clear and concise syntax, and a vast community that provides numerous helpful libraries and frameworks.

 - IDE Used: PyCharm is the IDE mentioned and used for developing and managing the project. PyCharm is a popular IDE for Python development, offering extensive support for Python, integration with various version control systems, web development tools, and support for test-driven development, making it ideal for projects involving Selenium and Behave.

**Libraries Chosen:** 

- selenium (A powerful library for automating web browsers, used to control the browser and interact with web elements)

- behave (Behavior-Driven Development testing framework for Python, allowing tests to be written in a language close to natural, based on scenarios)

- behave-html-formatter(useful for generating HTML reports from Behave tests) 

- webdriver-manager (an easy way to manage browser drivers (Chrome, Firefox, etc.) for Selenium tests, facilitating the automation of driver downloads and management)

- requests (library is highly regarded for its simplicity and ease of use for sending HTTP requests)

**Plugin Chosen:**

- pytest-html (This is a pytest plugin that generates HTML reports for test results)

- gherkin (Provides support for the specific syntax of Gherkin used in .feature files)

- ini (Useful for managing and editing INI configuration files)

_To install all the mentioned libraries and plugins, you can run the following commands in your command line interface:_
pip install ...


**Project Structure Overview**

- /.venv (Contains the virtual environment where dependencies such as Selenium, Behave, and others are isolated from the global Python environment, ensuring project consistency and preventing version conflicts)

- /features (Hosts .feature files which define the user stories and testing scenarios using Gherkin syntax. For example, search.feature includes scenarios like "Successful product search" and "Search for a non-existent product," which test different search functionalities on the e-commerce site)

- /pages (This directory utilizes the Page Object Model to encapsulate the functionality of each page. For instance, login_page.py defines methods like set_email() and click_login_button() that abstract the details of web page interactions, making the steps reusable and tests easier to maintain)

- /steps (Contains Python scripts such as login_steps.py and search_steps.py where the steps defined in the .feature files are implemented. These scripts make use of methods from /pages to execute actions described by each step in the feature files)

- behave.ini (A configuration file that sets up how Behave runs tests, including paths, formats, and other options that tailor the test execution environment)

- behave-report.html (An output HTML report generated post-test execution, detailing which tests passed or failed, thus providing actionable feedback to developers and testers)

- browser.py (Manages the WebDriver setup for Selenium, crucial for initiating and controlling browser sessions, demonstrated by initializing a Chrome browser instance configured to certain specifications)

- environment.py (Responsible for setting up and tearing down the test environment before and after test runs. It initializes instances like Browser, LoginPage, and other page objects, ensuring they are available throughout the test lifecycle)


_**Running Tests in the project:**_

- To run the tests we need to make sure that we have the libraries and plugins that we presented installed in our IDE.

- Running Tests in console

- Run All Tests - To execute all tests use this command in Terminal: behave

- Run a Single Feature - Run tests for a specific feature use: behave features/login.feature

- Run Tests with Specific Tags - If you want to run only the tests marked with a specific tag, such as @smoke, use the command: behave --tags=@smoke


**Checking Results:**
After test execution, results will be displayed in the console. Additionally, you can generate detailed HTML reports using:
behave -f html -o report.html (This command creates a report.html file that contains a detailed report of the test results, including executed scenarios, the steps taken, and the outcomes of each step.)

**Conclusion**

- In this project, we developed and executed a comprehensive suite of automated tests covering the fundamental functionalities of an e-commerce website.
- The test cases cover approximately 80% of the functional requirements. This includes critical user interactions such as searching for products, adding items to the shopping cart, registering new user accounts, and user login functionalities
- This project has successfully demonstrated the effectiveness of BDD in ensuring application quality and meeting user expectations

**_This project was made by: Raica Catalin Adrian_**






