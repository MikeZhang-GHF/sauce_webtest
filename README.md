# Sauce Webtest Project

## Design

### Page Object design pattern

PO pattern helps to write high cohesion and low coupling code. Moreover, PO also make the code easier to be reusable. Once the page objects are implemented, they are applied both in the webtest and the bdd test.
We used three layers for the implementation of PO pattern. 

1. UI element locating layer
2. Page service layer
3. Testcase(core functional test) layer

The main reason is to limit the impact to other layer once changes happen in one layer and apply the single responsibility principle.

- UI element locating layer, put the locating strategy for all the elements needed in the yaml file or python file(in special cases). A lot of changes could happen for the front end development. Once the UI element changes, we can only change the yaml file, limiting the impact to the other two layers. 
Please refer to the elementlocator directory for detailed information.

- Page service layer, we encapsulated the services that each page can offer, the interaction with users, such as click the element, input the information, get the text of the element, upload of file, etc. In addition, we applied the smart wait strategy for the target elements once the network is slow and also the exception handling once errors happens on the page. This layer encapsulate the details of operation of each UI element and only provide the interface for interaction, limiting the impact to the testcase layer.
Please refer to the page directory for detailed information.

- Testcase layer, functional test, call the services of page service layer to implement the functional test or other business processes.
Please refer to the testcase directory for detailed information.

- We also customized the browsers on the basis of Selenium webdriver, including the Chrome, Firefox, Edge, Safari, which covers the main stream web browsers in the market. We can apply the compatibility tests for these browsers.
Please refer to the browser file under util directory.

## Test Framework for Web and BBD Test

- We used pytest framework to manage and run testcases for the automation webtest. In addition, we also used the pytest distributed plugins to speed up the testing. Also, we applied the pytest markers to group the testcases to different functional tests. In addition, we used data driven test technique to test the same function by using different test cases. 
Please refer to the pytest.ini for pytest configuration and the testdata directory for the data driven test data.

- We also applied the pytest fixture in automation test and BDD test to reuse the code efficiently.
	
- Regarding the behavior driven test, we used the Behave framework and Gherkin syntax for the test. Please refer to the feature files and steps under features directory for detailed information.

- For the test report, we used the  Allure report plugins to present the test results. 
	
## CI/CD
- We used the gitHub actions to trigger the automation web test and BDD test. Please refer to the webtest.yml under .gitHub/workflows directory for detailed information. 
- The CI results are under Actions link of gitHub repo. The tests will be triggered by the push to main or branch and every hour.
- The test can also be triggered by the push of other repos, such as development team push the commit to their repos.
- Web test report is using [GitHub Pages](https://mikezhang-ghf.github.io/sauce_webtest/html/#).

