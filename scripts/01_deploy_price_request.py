#!/usr/bin/python3
from brownie import PriceContract, config, network
from scripts.helpful_scripts import (
    get_verify_status,
    get_account,
    get_contract,
)


def deploy_price_feed_request():
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
    )
    print(f"The current price of BTC is {price_feed.getLatestPrice()}")
    print(f"Higher? {price_feed.priceFeedGreater()}")
    return price_feed


def main():
    deploy_price_feed_request()
