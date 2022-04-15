**Scope of the project:**

Create a CI/CD process for your AF application. The CI pipeline should make a build, execute unit tests and create an artifact, which should be used in the CD pipeline.
The tests should be published.
The CD pipeline should start automatically after the CI pipeline was finished successfully. It should be first deployed to an Integration Environment, where
it should execute Integration tests. Afterwards it should be released to PROD (Manual Approval).

Useful information:

`pr: Pull request trigger, so that every time we make a pull request to the branch, the pipeline will be getting started automatically.`

`pool: In order to run a pipeline, we need an agent, which is a server with the necessary operating systems and tools, that will make our job run properly. Using Azure Devops Service we can make us of self-hosted Microsoft agents, we just need to define an operating system under "pool".`

`$Build.SourcesDirectory - main foder of our repo unit test - the process of checking small pieces of code (eg. functions) unittest.mock - mock objects can simulate the behavior of complex, real objects (eg. we can check whether a blob is being created in blob storage) assert - used to ensure that the code is behaving as expected`

`ArchiveFiles@2: Used in order to create build artifacts. $Build.ArtifactsStagingDirectory - the local path on the agent where any artifacts are copied to before being pushed to their destination`

`publish: Used to publish the artifacts. By default, they are being saved into $System.ArtifactsDirectory`

`AzureFunctionApp@1: Deploys the function.`
