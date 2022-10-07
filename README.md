# Myobservatory_app
I'm glad you came to visit my project, let me give you a guide. The framework of API testing consists of six parts：
 1.base: Define a base class for other page classes to inherit from.
 2.page: We encapsulate pages of system. Each page consists of three parts: 
  1.object library
  2.operational level
  3.business level
 3.report: the allure generates the test report in here.
 4.scripts: we write the test cases in here.
 5.utils: we encapsulate some methods that we commonly use.
This framework is simple and flexible, and it also integrates well with Jenkins.
