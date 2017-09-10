angular.module('movieApp.services',[]).factory('Movie',function($resource){
    return $resource('/movie/api/movie/:id',{id:'@id'},{
        update: {
            method: 'PUT'
        }
    });
}).service('popupService',function($window){
    this.showPopup=function(message){
        return $window.confirm(message);
    }
});
