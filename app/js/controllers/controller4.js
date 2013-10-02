function AdminCtrl($scope, $http, $location,$window) {
    /*$http.get('/api/user/me')
        .success(function (data) {
            $scope.user = data;
        })
        .error(function (data) {
            $location.path('/api/user/login')
        });*/
    $http.get('/rest/surveys').success(function(data) {
        $scope.surveys = data;
    })
    $scope.send = function(survey){
        $http.put('/rest/surveys',survey).success(function(data){
            $window.alert('Data saved with id '+data.key);
        })
    }
}