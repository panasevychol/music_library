var app = angular.module("app", []);

app.controller("MainController", function($scope, $http) {
  // Get artists
  $http.get('/artists/browse/', {params: {page_size: 3}} ).then(function(response){
    $scope.artists = response.data.results;
  });
  // Get releases
  $http.get('/releases/browse/', {params: {page_size: 3}} ).then(function(response){
    $scope.releases = response.data.results;
  });
});
