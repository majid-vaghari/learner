var myApp = angular.module('myApp', ['cfp.hotkeys']);

myApp.controller('mycontroller', ['$scope', '$http', 'hotkeys', function ($scope, $http, hotkeys) {

    $scope.finished = false;

    $scope.nextPic = function () {
        $scope.picId = $scope.nextId;
        $http.get('/next/' + $scope.picId)
            .success(function (result) {
                if (result.nextId != 'null')
                    $scope.nextId = result.nextId;
                else
                    $scope.finished = true;
            });
    };

    $scope.skip = function () {
        $scope.nextPic();
    };

    $scope.submit = function (num) {
        $http.get('/save/' + $scope.picId + '/' + num);
        $scope.nextPic();
    };


    hotkeys.add({
        combo: '0',
        callback: function () {
            $scope.submit(0);
        }
    });
    hotkeys.add({
        combo: '1',
        callback: function () {
            $scope.submit(1);
        }
    });
    hotkeys.add({
        combo: '2',
        callback: function () {
            $scope.submit(2);
        }
    });
    hotkeys.add({
        combo: '3',
        callback: function () {
            $scope.submit(3);
        }
    });
    hotkeys.add({
        combo: '4',
        callback: function () {
            $scope.submit(4);
        }
    });
    hotkeys.add({
        combo: '5',
        callback: function () {
            $scope.submit(5);
        }
    });
    hotkeys.add({
        combo: '6',
        callback: function () {
            $scope.submit(6);
        }
    });
    hotkeys.add({
        combo: '7',
        callback: function () {
            $scope.submit(7);
        }
    });
    hotkeys.add({
        combo: '8',
        callback: function () {
            $scope.submit(8);
        }
    });
    hotkeys.add({
        combo: '9',
        callback: function () {
            $scope.submit(9);
        }
    });
    hotkeys.add({
        combo: 'enter',
        callback: function () {
            $scope.skip();
        }
    });
    hotkeys.add({
        combo: 'space',
        callback: function () {
            $scope.skip();
        }
    });
}]);