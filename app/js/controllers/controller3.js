function ResultCtrl($scope, $http, $routeParams) {
  $http.get('/rest/result/'+$routeParams.resultKey).success(function(data) {
       $scope.result = data;
  });
}