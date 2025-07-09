# Database Seeding Guide - AWS Simulados

## Unified Database Seeder

The `unified_seed_database.py` script combines all database seeding functionality from the various individual scripts into a single, comprehensive tool.

### What it unifies:
- `generate_300_questions.py` - Bulk question generation
- `generate_additional_questions.py` - Additional practical questions
- `generate_clf_questions.py` - CLF-specific questions
- `generate_comprehensive_questions.py` - Comprehensive questions for all certifications
- `init_db.py` - Database initialization with sample questions
- `populate_questions.py` - Manual/sample questions

### Features:
- ✅ Seeds all certifications (CLF-C02, AIF-C01, SAA-C03, SAP-C02)
- ✅ Prevents duplicate questions
- ✅ Supports selective seeding by certification
- ✅ Database reset capability
- ✅ Verbose logging
- ✅ Comprehensive error handling
- ✅ Statistics reporting

## Usage

### Prerequisites
1. Ensure you're in the `aws-simulados-api` directory
2. Activate the virtual environment: `source bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

### Basic Usage

```bash
# Seed all certifications
python unified_seed_database.py

# Seed only CLF-C02
python unified_seed_database.py --cert CLF-C02

# Reset database and seed all
python unified_seed_database.py --reset

# Verbose output
python unified_seed_database.py --verbose

# Help
python unified_seed_database.py --help
```

### Examples

```bash
# Seed everything from scratch
python unified_seed_database.py --reset --verbose

# Add only AIF-C01 questions
python unified_seed_database.py --cert AIF-C01 --verbose

# Update database with any new questions
python unified_seed_database.py
```

### Command Line Options

- `--cert CERT`: Seed only specific certification (CLF-C02, AIF-C01, SAA-C03, SAP-C02)
- `--reset`: Clear existing questions before seeding
- `--verbose`: Enable detailed logging
- `--help`: Show help message

### Output

The script provides detailed statistics:
- Number of questions added
- Number of existing questions skipped
- Error count
- Questions by certification
- Total questions in database

### Question Sources

The unified script includes questions from:

1. **CLF-C02 (AWS Cloud Practitioner)**
   - Core concepts, security, technology, billing
   - ~50+ questions covering all domains

2. **AIF-C01 (AWS AI Practitioner)**
   - AI/ML fundamentals, AWS AI services, responsible AI
   - ~20+ questions covering key topics

3. **SAA-C03 (Solutions Architect Associate)**
   - Resilient architectures, high-performance, security, cost optimization
   - ~15+ questions covering core domains

4. **SAP-C02 (Solutions Architect Professional)**
   - Complex solutions, migration, cost control, continuous improvement
   - ~10+ questions covering advanced topics

### Database Schema

Questions are stored with the following structure:
- `certification`: Target certification (CLF-C02, AIF-C01, etc.)
- `domain`: Knowledge domain/category
- `question_text`: The question content
- `question_type`: multiple_choice or multiple_response
- `options`: JSON array of answer options
- `correct_answers`: JSON array of correct answers
- `explanation`: Detailed explanation of the answer
- `difficulty`: easy, medium, or hard

### Error Handling

The script includes comprehensive error handling:
- Duplicate question detection
- Database connection errors
- Malformed question data
- JSON serialization issues

### Migration from Old Scripts

After using the unified script, you can optionally:
1. Archive old individual scripts
2. Update deployment scripts to use the unified version
3. Update documentation to reference the new script

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure you're in the correct directory and virtual environment is active
2. **Database connection**: Verify database is accessible and permissions are correct
3. **Duplicate questions**: Script automatically handles duplicates by skipping them

### Verification

To verify the seeding worked correctly:

```bash
# Check question counts
python -c "
from src.main import app
from src.models.question import Question
with app.app_context():
    for cert in ['CLF-C02', 'AIF-C01', 'SAA-C03', 'SAP-C02']:
        count = Question.query.filter_by(certification=cert).count()
        print(f'{cert}: {count} questions')
"
```

## Next Steps

1. Test the unified script in your environment
2. Update deployment/CI scripts to use the unified version
3. Archive old individual scripts
4. Update team documentation
