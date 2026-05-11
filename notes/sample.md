# Heading 1

- Orange
- Banana
- Apple

## Heading 2

1. First
2. Second
3. Third

a. Chikatla
b. Purna 
c. Chand

- [Join Devops](https://learn.joindevops.com/learn)
- ![Image](https://in.images.search.yahoo.com/search/images;_ylt=Awr1UZcxSQFqSgIA6Na7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3Nj?type=E210IN1589G0&p=7+horses+image&fr=mcafee&th=316&tw=474&imgurl=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp8298164.jpg&rurl=https%3A%2F%2Fwallpapercave.com%2Frunning-seven-horses-wallpapers&size=221KB&name=Running+Seven+Horses+Wallpapers+-+Wallpaper+Cave&oid=1&h=1000&w=1500&turl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.aKTf6Wog3TCF-kg8QNRzfgHaE8%3Fpid%3DApi&tt=Running+Seven+Horses+Wallpapers+-+Wallpaper+Cave&sigr=19FRukj5uS1T&sigit=V1305ArOBRm_&sigi=Jk36NfoIEV8V&sign=n41gulLS_xUi&sigt=n41gulLS_xUi)
### Heading 3

- To write a command: `sh helloworld.sh`

##### Heading 4

```yaml
- name: Install cart component
  hosts: cart
  become: yes
  tasks:
  - name: setup NPM source
    ansible.builtin.shell: "curl -sL https://rpm.nodesource.com/setup_lts.x | bash"

  - name: Install NodeJS
    ansible.builtin.yum:
      name: nodejs
      state: installed
```
###### Heading 5

###### Heading 6