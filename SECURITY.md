# 🔒 Security Policy

## 📋 Supported Versions

We actively support and provide security updates for the following versions:

| Version | Supported | Status |
|---------|-----------|--------|
| > 1.0.x | ✅ | Actively maintained |
| < 1.0.0 | ❌ | No longer supported |

## 🚨 Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please help us protect our users by following these steps:

### 📝 How to Report

1. **Create a GitHub Issue** with the `vulnerability` label
2. **Include the following information:**
   - 🔍 Description of the vulnerability
   - 📍 Location in the codebase (file/line number if known)
   - 🎯 Steps to reproduce the issue
   - 💥 Potential impact
   - 🛠️ Suggested fix (if you have one)

### 🎖️ Recognition

We appreciate security researchers who help keep our project safe. Contributors who report valid security issues will be:
- ✨ Acknowledged in our release notes (unless you prefer to remain anonymous)
- 🙏 Thanked in our CHANGELOG

### 🔐 Security Best Practices

When using ibmdiagrams:
- ⚠️ Never commit sensitive data (credentials, API keys) to diagram code
- 🔄 Keep your installation up to date with the latest version
- 📚 Review our documentation for secure usage patterns
- 🔑 **Sign your commits with GPG** to verify authenticity and prevent impersonation (required for main branch contributions)

### 🔏 Commit Signing

To maintain code integrity and verify contributor identity, we require GPG-signed commits for all contributions to the main branch.

**Why sign commits?**
- ✅ Verifies commit authenticity
- ✅ Prevents commit impersonation
- ✅ Provides audit trail for compliance
- ✅ Builds trust in codebase integrity

**Setup instructions:**
See the [Setup GPG Signing](CONTRIBUTING.md#setup-gpg-signing) section in our Contributing Guide for detailed instructions on configuring GPG commit signing.

**Quick verification:**
```bash
# Check if your commits are signed
git log --show-signature -1
```

---

**Thank you for helping keep ibmdiagrams secure! 🛡️**
