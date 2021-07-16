from brownie import PriceContract, config, network
import time
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account


def test_can_get_latest_price():
    account = get_account()
    btc_usd_price_feed_address = get_contract("btc_usd_price_feed").address
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    oracle = get_contract("oracle").address
    link_token = get_contract("link_token").address
    price_feed = PriceContract.deploy(
        oracle,
        jobId,
        fee,
        link_token, btc_usd_price_feed_address,
        {"from": account},
        publish_source=get_verify_status(),
    # Assert
    value=price_feed.getLatestPrice({"from": get_account()})
    assert isinstance(value, int)
    assert value > 0
