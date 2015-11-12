var  movieControllers = angular.module('movieControllers', []);
   
movieControllers.controller('movieListController', ['$scope', '$routeParams', '$http', 'Movie', 'popupService', '$window',  
    function($scope, $routeParams, $http, Movie, popupService, $window) {
    //$http.get('http://127.0.0.1:8000/movie/api/movie/' + $routeParams.movieId + '/?format=json')
    //.success(function(response) { $scope.movie = response; });
    $scope.movies=Movie.query();
    $scope.deleteMovie=function(movie){
        if(popupService.showPopup('Really delete this?')){
            movie.$delete({id: movie.id},function(){
                $window.location.href='';
            });
        }    
    }
}]).controller('movieCreateController',['$scope', '$http', 'Movie', '$location', 
	function($scope,$http,Movie, $location){

    $scope.movie=new Movie();
    $scope.addMovie=function(){
		console.log($scope.movie);
        $scope.movie.$save(function(){
            $location.url('/movies');
        });
    }
}]).controller('movieViewController', ['$scope','$routeParams', 'Movie',
	function($scope, $routeParams, Movie){
    $scope.movie=Movie.get({id:$routeParams.id});
    
}]).controller('movieEditController', ['$scope','$routeParams', 'Movie', '$location',
	function($scope, $routeParams, Movie, $location){

    $scope.updateMovie=function(){
        $scope.movie.$update(function(){
            $location.url('/movies');
        });
    };

    $scope.loadMovie=function(){
        $scope.movie=Movie.get({id:$routeParams.id});
    };

    $scope.loadMovie();
}]);
