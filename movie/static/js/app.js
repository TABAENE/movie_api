  // create the module and name it movieApp
    var movieApp = angular.module('movieApp', ['ngRoute', 'ngResource', 'movieControllers', 'movieApp.services']);
    
    movieApp.config(['$routeProvider', '$locationProvider', '$resourceProvider',
		function($routeProvider, $locationProvider, $resourceProvider){
		//$locationProvider.html5Mode({enabled: true, requireBase: false});
		//$resourceProvider.defaults.stripTrailingSlashes = false;
		$routeProvider
		.when('/movie', {templateUrl: '/static/templates/movie.html', controller: 'movieListController'})
		.when('/movie/:id/view', {templateUrl: '/static/templates/movie-view.html', controller: 'movieViewController'})
        .when("/movie/new", { templateUrl: "/static/templates/movie-add.html", controller: 'movieCreateController'})
        .when("/movie/:id/edit", { templateUrl: "/static/templates/movie-edit.html", controller: 'movieEditController'})
        .otherwise( { redirectTo: "/movie" });			
	}
    ]);

    movieApp.config(['$httpProvider',
		function($httpProvider){
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		$httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
	}
    ]);
    

movieApp.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
