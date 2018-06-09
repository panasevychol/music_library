var app = angular.module("app", []);

app.controller("MainController", function($scope, $http) {
  var itemsPerPage = 3;

  // Get artists
  $http.get('/artists/browse/', {params: {page_size: itemsPerPage}} ).then(function(response){
    $scope.artists = response.data.results;
  });
  // Get releases
  $http.get('/releases/browse/', {params: {page_size: itemsPerPage}} ).then(function(response){
    $scope.releases = response.data.results;
  });

  $scope.search = function(query) {

     // Get artists
     $http.get('/artists/browse/', {params: {search: query, page_size: itemsPerPage}} ).then(function(response){
       $scope.artists = response.data.results;
     });
     // Get releases
     $http.get('/releases/browse/', {params: {search: query, page_size: itemsPerPage}} ).then(function(response){
       $scope.releases = response.data.results;
     });

   };
});
