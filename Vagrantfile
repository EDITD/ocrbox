# OCR Box
# here we naively assume we have 4 CPU's available

Vagrant.configure('2') do |config|
    config.vm.box = 'ubuntu/trusty64'
    config.vm.synced_folder './', '/opt/ocrbox'

    # Give moar rams/cpu
    config.vm.provider 'virtualbox' do |v|
        v.memory = 1024
        v.cpus = 4
    end

    # Ansible provision
    config.vm.provision :ansible do |ansifail|
        ansifail.playbook = 'playbook/playbook.yml'
    end

    # Dev VM
    config.vm.define :ocrbox, primary: true do |ocrbox|
        ocrbox.vm.hostname = 'ocrbox'
        ocrbox.vm.provider 'virtualbox' do |v|
            v.name = 'ocrbox'
        end
    end
end
