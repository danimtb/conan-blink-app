def artifactory_name = "artifactory_local"
def artifactory_repo = "conan-local"
String docker_image = 'lasote/conangcc6-armv7'

node {
    docker.image(docker_image).inside('-v /tmp/:/tmp/ -v /home/danimtb/:/home/conan/danimtb/ --net=host') { 
        def server = Artifactory.server artifactory_name
        def client = Artifactory.newConanClient() 
        def serverName = client.remote.add server: server, repo: artifactory_repo
        
        stage("Get project") {
              checkout scm
//            sh 'cp -a /home/conan/danimtb/repos/conan-hello-app .'
//            git branch: repo_branch, url: repo_url
        }
        
        stage("Get dependencies and create app") {
            String strCommand = "create conan-hello-app/conanfile.py danimtb/testing -s arch=armv7"
            client.run(command: strCommand )
        }
        
        stage("Upload packages") {
            String command = "upload HelloApp* --all -r ${serverName} --confirm"
            def b = client.run(command: command)
            b.env.collect()
            server.publishBuildInfo b
        }
    }
}
