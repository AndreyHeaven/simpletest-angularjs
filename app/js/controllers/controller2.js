'use strict';

/* Controllers */

/*
angular.module('myApp.controllers').
  controller('MyCtrl2', ['$scope','$timeout', '$routeParams',function($scope, $timeout, $routeParams) {
    $http.get('/rest/survey/'+$routeParams.testKey).success(function(data) {
        $scope.answers = data;
    });
  }]);
*/


function AnswerCtrl($scope, $http, $routeParams) {
  $http.get('/rest/survey/'+$routeParams.testKey).success(function(data) {
      $scope.questions = data;
      $scope.index = 0;
      $scope.userAnswers = {};
      $scope.answer = '';
  });
  $scope.next = function(){
      var q = $scope.questions[$scope.index]
      $scope.userAnswers[''+q.id] = $scope.answer;
      $scope.index = $scope.index+1;
      $scope.answer = '';
      if ($scope.index > $scope.questions.length -1)
          $scope.index = 0;
  }
    $scope.finish = function(){
        var testKey = $routeParams.testKey;

        $http.put('/rest/result/'+testKey,$scope.userAnswers).success(function(data){
            $location.path('/view3/'+data.resultKey);
        })
    }
}

