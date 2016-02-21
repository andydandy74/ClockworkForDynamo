Some simple rules for posting issues and pull requests for Clockwork for Dynamo

### Issues
- **When posting bugs: Describe what you were doing, what went wrong and what you were expecting to happen.** Include screenshots where applicable.
- **Also when posting bugs: Describe your setup.** (Operating Sytem, Dynamo version, Revit version & build number) If you're using a daily build, please include the filename of the installer.
- **When posting wishes: Go wild.** After all, it's a wish, right?
- **Make sure you are running one of the *supported* Clockwork versions and it's the *latest available version** (see https://github.com/CAAD-RWTH/ClockworkForDynamo#versions)
- **Make sure your installed version of Clockwork matches the Dynamo version it's installed for** (e.g. Clockwork for Dynamo 0.8.x is *not* installed for Dynamo 0.9.x)
- **Make sure you do *not* have multiple versions of Clockwork installed for one Dynamo version** (e.g. Clockwork for Dynamo 0.7.x and Clockwork for Dynamo 0.8.x installed for the same Dynamo version). Please check your packages folder (typically C:\Users\YOUR_USER_NAME\AppData\Roaming\Dynamo\YOUR_DYNAMO_VERSION\packages)

### Pull Requests
- **Describe the purpose of your PR and what you have changed in the original code.**
- **Ensure the best possible maintenance.** Currently, most nodes are identical for the 0.8 and 0.9 versions of Clockwork - which means they are authored in Dynamo 0.8 and then distributed to both package versions. Only submit 0.9 nodes if they make use of functionality that is not available in Dynamo 0.8.
- **For 0.8 nodes: Do *not* submit anything authored in a post-0.8.2 build** (build numbers larger than 0.8.2.2392).
- **For 0.9 nodes: Do *not* submit anything authored in a post-0.9.0 build** (build numbers larger than 0.9.0.3067).
- **Make sure you are running one of the *supported* Clockwork versions and it's the *latest available version** (see https://github.com/CAAD-RWTH/ClockworkForDynamo#versions)
