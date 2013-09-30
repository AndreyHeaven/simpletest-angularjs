'use strict';


// Define all the modules and their dependencies
angular.module('myApp.filters', []);
angular.module('myApp.services', []);
angular.module('myApp.directives', []);
angular.module('myApp.controllers', []);

// Declare app level module which depends on filters, and services

angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives', 'myApp.controllers']).
  config(['$routeProvider','$locationProvider', function($routeProvider,$locationProvider) {

    $locationProvider.html5Mode(true).hashPrefix('!');

    $routeProvider.when('/', {templateUrl: '/partials/partial1.html', controller: TestListCtrl,resolve:TestListCtrl.resolve});
    $routeProvider.when('/view2/:testKey', {templateUrl: '/partials/partial2.html', controller: AnswerCtrl});
    $routeProvider.when('/view3/:resultKey', {templateUrl: '/partials/partial3.html', controller: 'MyCtrl3'});
    $routeProvider.otherwise({redirectTo: '/'});
  }]);


