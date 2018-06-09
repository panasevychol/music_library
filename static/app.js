var app = angular.module("app", []);

app.controller("HelloController", function($scope, $http) {
  // Get artists
  $http.get('/artists/browse/').then(function(response){
    $scope.artists = response.data.results;
  });
});
