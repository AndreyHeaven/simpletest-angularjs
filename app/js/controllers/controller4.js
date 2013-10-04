function AdminCtrl($scope, $http, $location,$window) {
    /*$http.get('/api/user/me')
        .success(function (data) {
            $scope.user = data;
        })
        .error(function (data) {
            $location.path('/api/user/login')
        });*/

	$scope.updateServeysList = function (){
	    $http.get('/rest/surveys').success(function(data) {
	        $scope.surveys = data;
	    });
	}
	$scope.updateServeysList();
    $scope.send = function(survey) {
        $http.put('/rest/surveys',survey).success(function(data){
            $scope.error = false;
            $scope.updateServeysList();
        }).error(function(){
        	$scope.error = true;
        });
    }
    $scope.getSurvey = function(survey){
        if (!survey)
            angular.copy({},$scope.survey)
        else
            $http.get('/rest/admin/survey/'+survey).success(function(data) {
                angular.copy(data,$scope.survey)
            });
    }
}