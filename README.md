# Sauce Webtest Project

## Design

### Page Object design pattern

PO pattern helps to write high cohesion and low coupling code. Moreover, PO also make the code easier to be reusable. Once the page objects are implemented, they are applied both in the webtest and the bdd test.

Three layers are used for the implementation of PO pattern. 

1. **UI element locating layer**
2. **Page service layer**
3. **Testcase(core functional test) layer**

The main reason is to limit the impacts to other layer once changes happen in one layer and apply the single responsibility principle.

- UI element locating layer, the locating strategy for all the elements needed are saved in the yaml files or python files(in special cases). A lot of changes could happen for the front end development. Once the UI element changes, we can only change the yaml file, limiting the impacts to the other two layers. 

Please refer to the [elementlocator](https://github.com/MikeZhang-GHF/sauce_webtest/tree/main/elementlocator) directory for detailed information.

- Page service layer, the services that each page can offer are encapsulated, for example, the interaction with users, such as click the element, input the information, get the text of the element, upload of file, etc. In addition, the smart wait strategy are applied for the target elements once the network is slow or unstable and the exceptions are handled once errors happens on the page. This layer encapsulate the details of operation of each UI element and only provide the interface for interaction, limiting the impact to the testcase layer.

Please refer to the [page](https://github.com/MikeZhang-GHF/sauce_webtest/tree/main/page) directory for detailed information.

- Testcase layer, functional test, call the services of page service layer to implement the functional test or other business processes.

Please refer to the [testcase](https://github.com/MikeZhang-GHF/sauce_webtest/tree/main/testcase) directory for detailed information.

- The browsers are customized on the basis of selenium webdriver, including the Chrome, Firefox, Edge, Safari, which covers the main stream web browsers in the market. The compatibility tests for these browsers could be applied.

Please refer to the [browser](https://github.com/MikeZhang-GHF/sauce_webtest/blob/main/util/browser.py) file under **util** directory.

## Test Framework for Web and BBD Test

- Pytest framework are used to manage and run testcases for the automation web test. In addition, the pytest distributed plugins are used to speed up the testing. Also, the pytest markers are used to group the testcases for the different functional tests. In addition, data driven test technique are used to test the same function by using different test cases. 

Please refer to the [pytest.ini](https://github.com/MikeZhang-GHF/sauce_webtest/blob/main/pytest.ini) for pytest configuration and the **testdata** directory for the data driven test data.

- The pytest fixture are used in automation test and BDD test in order to reuse the code efficiently.
	
- Regarding the behavior driven test, the Behave framework and Gherkin syntax are used for the bdd test. Please refer to the [features](https://github.com/MikeZhang-GHF/sauce_webtest/tree/main/features) files and [steps](https://github.com/MikeZhang-GHF/sauce_webtest/tree/main/features/steps) under features directory for detailed information.

- For the test report, the allure plugins is used to present the test results. 
	
## CI/CD
- The gitHub actions are used to trigger the automation web and BDD test. Please refer to the **webtest.yml** under [.gitHub/workflows](https://github.com/MikeZhang-GHF/sauce_webtest/tree/main/.github/workflows) directory for detailed information. 
- The CI results are under [Actions](https://github.com/MikeZhang-GHF/sauce_webtest/actions) link of gitHub repo. The tests will be triggered by the push to main or branch and scheduled to run every hour.
- The test can also be triggered by the push of other repos, such as development team push the commit to their repos.
- Web test report is using [GitHub Pages](https://mikezhang-ghf.github.io/sauce_webtest/html/#).

