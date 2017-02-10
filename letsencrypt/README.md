This is just some hacky plumbing that Tristan wrote to get letsencrypt working.
This is for using certbot in manual mode.
To use set environment variables in heroku for the ACME challenge and reply like this:
ACME_CHALLENGE_NAME='-n-BxAzt86gbCDfc9L5FwLJ9tU93GvNGGftVtPdnzio'
ACME_CHALLENGE_KEY='-n-BxAzt86gbCCfc9L5FwLJ9tU93GvOGGftVtPdnzio.980gabmoiPlzkd6fkuSqq7n4IKdUNsHEZVh3SbiZ3ZQ'
