var app = angular.module("app", []);

app.controller("MainController", function($scope, $http) {
  var itemsPerPage = 3;

  $scope.showHomefeed = function() {

    // Get artists
    $http.get('/artists/browse/', {params: {page_size: itemsPerPage}} ).then(function(response){
      $scope.artists = response.data.results;
    });
    // Get releases
    $http.get('/releases/browse/', {params: {page_size: itemsPerPage}} ).then(function(response){
      $scope.releases = response.data.results;
    });
    // Get tracks
    $http.get('/tracks/browse/', {params: {page_size: 10}} ).then(function(response){
      $scope.tracks = response.data.results;
    });
    $scope.view = 'feed';
  };

  $scope.search = function(query) {

     // Search artists
     $http.get('/artists/browse/', {params: {search: query, page_size: itemsPerPage}} ).then(function(response){
       $scope.artists = response.data.results;
     });
     // Search releases
     $http.get('/releases/browse/', {params: {search: query, page_size: itemsPerPage}} ).then(function(response){
       $scope.releases = response.data.results;
     });
     // Search tracks
     $http.get('/tracks/browse/', {params: {search: query, page_size: 10}} ).then(function(response){
       $scope.tracks = response.data.results;
     });
     $scope.view = 'feed';
   };

   $scope.showArtistDetails = function(artist) {
      $scope.artist = artist;

      // Get artist releases
      $http.get('/releases/browse/', {params: {artist: artist.slug, page_size: itemsPerPage}} ).then(function(response){
        $scope.artist.releases = response.data.results;
      });
      // Get tracks
      $http.get('/tracks/browse/', {params: {artist: artist.slug, page_size: 10}} ).then(function(response){
        $scope.artist.tracks = response.data.results;
      });
      $scope.view = 'artist';
    };

  $scope.showReleaseDetails = function(release) {
     $scope.release = release;

     // Get tracks
     $http.get('/tracks/browse/', {params: {release: release.id, page_size: 0}} ).then(function(response){
       $scope.release.tracks = response.data.results;
     });
     $scope.view = 'release';
   };

   $scope.showHomefeed();
});
