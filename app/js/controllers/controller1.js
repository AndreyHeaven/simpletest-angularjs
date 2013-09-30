'use strict';

/* Controllers */

/*
angular.module('myApp.controllers').
  controller('MainCtrl', ['$scope','$timeout','$http',function($scope, $timeout,$http) {
    $http.get('/rest/surveys').success(function(data) {
        $scope.surveys = data;
    });

  }]);*/

function TestListCtrl($scope, surveys) {
  $scope.surveys = surveys;
}

TestListCtrl.resolve = {
  surveys: function($http, $q) {
    var deferred = $q.defer();
    //выполняем запрос на получение данных
    //если данные успешно приняты выполним  deferred.resolve()
    //если произошла ошибка выполним deferred.reject()
      $http.get('/rest/surveys').success(function(data) {
        deferred.resolve(data);
    }).error(function(){
              deferred.reject();
          });
    return deferred.promise;
  },
  delay: function($q, $timeout) {
    var delay = $q.defer();
    $timeout(delay.resolve, 1000);
    return delay.promise;
  }
}