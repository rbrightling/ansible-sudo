SUDO
====

Install sudo and manage main sudoers configuration. 

**Recommendations**: Set requiretty globally and specify only ansible user to not requiretty.

Best practice security has tried to be applied to the default configurations; however, always ensure sufficiant 
scrutiny as this is no guarantee.

It can often be best to create role specific configuration for sudoers under the /etc/sudoers.d directory.

Requirements
------------

Supported OS's
  - Debian 10
  - Centos 8

Role Variables
--------------

```yaml
# defaults file for sudo

# Global Defaults (Boolean)
sudo_always_set_home: true
sudo_env_editor: true
sudo_env_reset: true
sudo_mail_badpass: true
sudo_match_group_by_gid: true
sudo_requiretty: false
sudo_visiblepw: false

sudo_query_group_plugin: null
sudo_authenticate: null
sudo_closefrom_override: null
sudo_compress_io: null
sudo_exec_background: null
sudo_fast_glob: null
sudo_fqdn: null
sudo_ignore_dot: null
sudo_ignore_local_sudoers: null
sudo_insults: null
sudo_log_input: null
sudo_log_output: null
sudo_log_year: null
sudo_long_opt_prompt: null
sudo_mail_all_cmnds: null
sudo_mail_always: null
sudo_mail_no_host: null
sudo_mail_no_perms: null
sudo_mail_no_user: null
sudo_netgroup_tuple: null
sudo_noexec: null
sudo_pam_session: null
sudo_pam_setcred: null
sudo_passprompt_override: null
sudo_path_info: null
sudo_preserve_groups: null
sudo_pwfeedback: null
sudo_root_sudo: null
sudo_rootpw: null
sudo_runaspw: null
sudo_set_home: null
sudo_set_logname: null
sudo_set_utmp: null
sudo_setenv: null
sudo_shell_noargs: null
sudo_stay_setuid: null
sudo_sudoedit_checkdir: null
sudo_sudoedit_follow: null
sudo_targetpw: null
sudo_tty_tickets: null
sudo_umask_override: null
sudo_use_loginclass: null
sudo_use_netgroups: null
sudo_use_pty: null
sudo_utmp_runas: null

# Global Defaults (Integer)
sudo_closefrom: null
sudo_maxseq: null
sudo_passwd_tries: null

# Global Defaults (Interger, Boolean)
sudo_loginelen: null
sudo_passwd_timeout: null
sudo_timestamp_timeout: 5
sudo_umask: null

# Global Defaults (String)

sudo_editor: "{{ sudo__editor }}"
# Redhat:
#   - /usr/bin/vi
#   - /usr/bin/vim
#   - /usr/bin/nano
# Debian:
#   - /usr/bin/editor
#   - /usr/bin/vim
#   - /usr/bin/vi
#   - /usr/bin/nano
#   -/usr/bin/vim.tiny

sudo_badpass_message: null
sudo_iolog_dir: null
sudo_iolog_file: null
sudo_lecure_status_dir: null
sudo_limitprivs: null
sudo_mailsub: null
sudo_noexec_file: null
sudo_pam_login_service: null
sudo_pam_service: null
sudo_passprompt: null
sudo_privs: null
sudo_role: null
sudo_runas_default: null
sudo_syslog_badpri: null
sudo_syslog_goodpri: null
sudo_sudoers_locale: null
sudo_timestampdir: null
sudo_timestampowner: null

# Global Defaults (String, Boolean)
sudo_secure_path: "/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin"

sudo_type: null
sudo_exempt_group: null
sudo_group_plugin: null
sudo_lecture: null
sudo_lecture_file: null
sudo_listpw: null
sudo_logfile: "/var/log/sudo.log"
sudo_mailerflags: null
sudo_mailerpath: null
sudo_mailerfrom: null
sudo_mailto: null
sudo_syslog: null
sudo_verifypw: null

# Global Defaults (Lists, Boolean)
sudo_env_keep: 
  - SUDO_EDITOR
  - EDITOR
  - PS1
  - PS2
  - LS_COLOURS
  - USERNAME
  - LANG
  - LC_ADDRESS
  - LC_CTYPE
  - LC_COLLATE
  - LC_IDENTIFICATION
  - LC_MEASUREMENT
  - LC_MESSAGES
  - LC_MONETARY
  - LC_NAME
  - LC_NUMERIC
  - LC_PAPER
  - LC_TELEPHONE
  - LC_TIME
  - LC_ALL
  - LANGUAGE

sudo_env_check: null
sudo_env_delete: null
sudo_group_file: null
sudo_system_group: null


# Alias format:
# Dictionary Key will be UPPERCASED and take a list of aliases
sudo_host_aliases: {}
sudo_cmnd_aliases: {}
sudo_user_aliases: {}
# Example:
# fulltimers:
#   - millert
#   - mikef
#   - dowdy


# Defaults Format
sudo_user_defaults: {}
sudo_runas_defaults: {}
sudo_host_defaults: {}
sudo_cmnd_defaults: {}
# Example:
#   name: 
#     option: value
#
# Example value types:
# Set String:
#     secure_path: "/usr/bin:/bin"
# Set List:
#     secure_path:
#       - "/usr/bin"
#       - "/bin"
#
# To add or remove from a list.
# String:
#     secure_path: "+=/usr/local/bin -=/usr/sbin:/sbin"
# List
#     secure_path: 
#       - +/usr/local/bin
#       - -/usr/sbin
#       - -/sbin

# Sudo Users format
#
# List of dictionaries with the following keys:
#   name: [String](Required) Name of the target user for the sudo rule
#   type: [user, uid, group, gid, netgroup, nonunix_group, noneunix_gid](Optiona) target type.
#   hosts: [String](Optional)(Default: ALL): Hosts the user can run sudo on
#   runas_user: [String](Option): Who the target can run the command as
#   runas_group: [String](Option): The group the target can run the command as
#   commands: [String, List](Option)(Default: ALL): The commands allowed to be run as sudo
#
sudo_users: []
# Example:
#   - name: example1
#   - name: example2
#     type: group
#     runas_user: www
#     tags:
#       - nopasswd
#     commands:
#       - ALL
#       - "!/usr/bin/su"
# Output:
#   example1 ALL =  ALL
#   %example2 ALL = (www) NOPASSWD: ALL, !/usr/bin/su

# Sudoers default root user entry.
# Can be disabled setting to false
sudo_root_user:
  hosts: ALL
  runas_user: ALL
  runas_group: ALL
  commands: ALL


# Sudoers default sudo group user entry.
# Can be disabled setting to false
# Debian: name = sudo
# Redhat: name = wheel
sudo_sudo_group:
  hosts: ALL
  runas_user: ALL
  runas_group: ALL
  commands: ALL
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Include sudo"
      include_role:
        name: sudo
```

Example without global requiretty.
```yaml
- hosts: servers
  tasks:
    - name: "Include sudo"
      include_role:
        name: sudo
      vars:
        sudo_requiretty: true
        sudo_user_defaults:
          ansible_user:
            requiretty: false
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
