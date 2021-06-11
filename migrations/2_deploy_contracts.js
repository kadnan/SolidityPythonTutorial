const FirstContract=artifacts.require ('./FirstContract.sol');
module.exports = function(deployer) {
      deployer.deploy(FirstContract);
}