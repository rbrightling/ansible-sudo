import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_openssh_server_installed(host):
    sudo_package_name = "sudo"
    sudo_package = host.package(sudo_package_name)
    assert sudo_package.is_installed
