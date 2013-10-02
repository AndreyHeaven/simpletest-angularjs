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
            $window.alert('Data saved with id '+data.key);
            $scope.updateServeysList();
        }).error(function(){
        	$window.alert('ERROR');
        });
    }
    $scope.getSurvey = function(survey){
	    $http.get('/rest/admin/survey/'+survey.code).success(function(data) {
	    	angular.copy(data,$scope.survey)
	    });
//    	
    }
}