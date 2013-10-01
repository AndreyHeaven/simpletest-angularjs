function ResultCtrl($scope, $http, $routeParams, $location) {
    $scope.location = $location.absUrl();
    $http.get('/rest/result/' + $routeParams.resultKey).success(function (data) {
        $scope.result = data;
    });
}