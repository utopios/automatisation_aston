from ansible.module_utils.basic import *
def main():
    module = AnsibleModule(argument_spec={})
    # build module
    module.exit_json(True, {"result", "action from out first module"})


if __name__ == '__main__':
    main()