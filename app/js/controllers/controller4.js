function AdminCtrl($scope, $http, $location) {
    $http.get('/api/user/me')
        .success(function (data) {
            $scope.user = data;
        })
        .error(function (data) {
            $location.path('/api/user/login')
        });
}